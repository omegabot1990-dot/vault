const { Plugin, Notice } = require('obsidian');

class MyPlugin extends Plugin {
    onload() {
        console.log('Loading YAML Validator plugin');

        // Dynamically load js-yaml from CDN
        this.loadJsYaml(() => {
            this.registerEvent(
                this.app.vault.on('modify', this.validateYamlFrontmatter.bind(this))
            );
        });
    }

    loadJsYaml(callback) {
        const script = document.createElement("script");
        script.src = "https://cdn.jsdelivr.net/npm/js-yaml@4.1.0/dist/js-yaml.min.js";
        script.onload = () => {
            console.log("js-yaml loaded");
            callback();
        };
        document.head.appendChild(script);
    }

    validateYamlFrontmatter(file) {
        if (file.extension !== 'md') return;

        this.app.vault.read(file).then(content => {
            const frontmatter = this.getYamlFrontmatter(content);
            if (frontmatter) {
                this.validateFrontmatter(frontmatter, file);
            }
        });
    }

    getYamlFrontmatter(content) {
        const yaml = content.match(/^---\n([\s\S]*?)\n---/);
        if (yaml) {
            try {
                return jsyaml.load(yaml[1]);
            } catch (e) {
                console.error('Error parsing YAML:', e);
            }
        }
        return null;
    }

    validateFrontmatter(frontmatter, file) {
        const validationRules = {
            status: ['Backlog', 'To Do', 'In Progress', 'In Review', 'Done', 'Archive'],
            "urgency level": ['urgent', 'not urgent'],
            "importance level": ['important', 'not important'],
            "task type": ['capture', 'distil', 'organise', 'plan', 'execute']
        };

        let errorMessages = [];

        for (const property in validationRules) {
            if (frontmatter[property] && !validationRules[property].includes(frontmatter[property])) {
                // Constructing the error message
                const errorMessage = `The property "${property}" in file "${file.name}" contains an invalid value: "${frontmatter[property]}".
Valid values for "${property}" are: ${validationRules[property].join(', ')}. Please update the value accordingly.`;

                errorMessages.push(errorMessage);
            }
        }

        if (errorMessages.length > 0) {
            new Notice(errorMessages.join('\n'), 10000); // Error message will last for 10 seconds
        }
    }

    onunload() {
        console.log('Unloading YAML Validator plugin');
    }
}

module.exports = MyPlugin;
