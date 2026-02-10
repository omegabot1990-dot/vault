module.exports = async function(tp) {
    try {
        // Extract the parent nodes from the frontmatter
        const parentNodes = tp.frontmatter['parent nodes'];
        
        if (!parentNodes || parentNodes.length === 0) {
            throw new Error("No parent nodes found in frontmatter.");
        }

        // Extract and clean the first parent node title
        const parentNodeTitle = parentNodes[0].replace(/\[\[/g, '').replace(/\]\]/g, '');

        // Find the parent node file based on the title
        const parentNodeFile = await tp.file.find_tfile(parentNodeTitle);
        
        if (!parentNodeFile) {
            throw new Error(`Parent node file not found: ${parentNodeTitle}`);
        }

        // Get the folder path of the parent node file
        const parentNodeFolderPath = parentNodeFile.parent.path;
        
        // Get the current file title and construct the new path
        const childNodeTitle = tp.file.title;
        const newFilePath = `${parentNodeFolderPath}/${childNodeTitle}`;

        // Find the current file (child node) tfile object
        const childNodeFile = await tp.file.find_tfile(childNodeTitle);

        if (!childNodeFile) {
            throw new Error(`Child node file not found: ${childNodeTitle}`);
        }

        // Move the child node file to the new path under the parent node's folder
        await tp.file.move(newFilePath, childNodeFile);

        console.log(`Successfully moved ${childNodeTitle} to ${newFilePath}`);
    } catch (error) {
        // Log any errors that occur during the process
        console.error("Error occurred:", error.message);
    }
};
