module.exports = async function(tp) {
    try {
        const dv = app.plugins.plugins["dataview"].api;

        // Query tasks in the "002 - inbox" folder with status "Archive"
        const archiveQuery = dv.pages('"002 - inbox/raw"').where(p => p.status === "Archive");

        let archivedFiles = [];
        for (const page of archiveQuery) { 
            archivedFiles.push(page.file.name);
        }

        const archiveFolderPath = "600 - task manager/archive";

        for (const fileName of archivedFiles) {
            try {
                // Find the file (tfile) object based on its name
                const fileTFile = await tp.file.find_tfile(fileName);
                
                if (!fileTFile) {
                    throw new Error(`File not found: ${fileName}`);
                }

                // Construct the new file path in the archive folder
                const fileTitleWithoutExtension = fileTFile.name.replace(/\.md$/, '');
                const newFilePath = `${archiveFolderPath}/${fileTitleWithoutExtension}`;

                // Move the file to the new archive path
                await tp.file.move(newFilePath, fileTFile);

                console.log(`Successfully moved ${fileTitleWithoutExtension} to ${newFilePath}`);
            } catch (fileError) {
                console.error(`Error processing file ${fileName}: ${fileError.message}`);
            }
        }
    } catch (error) {
        // Log any general errors that occur during the process
        console.error("Error occurred:", error.message);
    }
};
