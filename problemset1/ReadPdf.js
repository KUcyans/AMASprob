const fs = require('fs');
const pdf = require('pdf-parse');

let dataBuffer = fs.readFileSync('authors-acknowledgements-v5.pdf');

pdf(dataBuffer).then(function(data) {
    let text = data.text;
    // Proceed to parse the text according to your requirements
});

function parseText(text) {
    // Normalize unicode to replace diacritic characters
    text = text.normalize("NFD").replace(/[\u0300-\u036f]/g, "");

    // Remove all numbers
    text = text.replace(/\d+/g, '');

    let lines = text.split('\n');

    // Initialize an array to hold the processed lines
    let processedLines = [];

    for (let i = 0; i < lines.length; i++) {
        let line = lines[i].trim();

        // Remove lines that only contain '(contents),' or similar patterns
        if (/^\(.*?\),?$/.test(line)) {
            continue;
        }

        // Remove lines that consist only of a comma
        if (line === ",") {
            continue;
        }

        // Remove "AND" and content in parentheses at the start of a line
        if (line.startsWith("AND")) {
            line = line.substring(3).trim();
            line = line.replace(/\(.*?\)/, "").trim();
        }

        // Correctly check if the line does not end with a comma
        if (!line.endsWith(',') && i < lines.length - 1) {
            // Add a space before concatenating the next line if it's not empty or just a comma
            let nextLine = lines[i + 1].trim();
            if (nextLine !== '' && nextLine !== ',') {
                line += " " + nextLine;
                i++; // Skip the next line since it's now part of the current line
            }
        }

        processedLines.push(line);
    }

    // Filter out empty lines
    processedLines = processedLines.filter(line => line.length > 0);

    return processedLines.join('\n');
}





pdf(dataBuffer).then(function(data) {
    let parsedText = parseText(data.text);
    fs.writeFileSync('resources/output.txt', parsedText);
});

