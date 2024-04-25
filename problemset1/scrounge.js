const fs = require('fs');
const fetch = require('node-fetch');
const path = require('path');

const dirResource = 'resources/';

const headers = {
    'User-Agent': 'Chrome/90.0.4430.212'
};

const scrounge = async () => {
    for (let year = 2009; year < 2025; year++) {
        let url = `https://kenpom.com/index.php?y=${year}`;

        if (year === 2024) {
            url = 'https://kenpom.com/';
        }

        try {
            const response = await fetch(url, { headers: headers });

            if (response.ok) {
                const text = await response.text();
                const filePath = path.join(dirResource, `${year}.html`);

                // Ensure the directory exists
                fs.mkdirSync(dirResource, { recursive: true });

                fs.writeFileSync(filePath, text, 'utf-8');
                console.log(`Saved HTML content for year ${year}`);
            } else {
                console.log(`Collection of stats in year ${year} failed. Err: ${response.status}`);
            }
        } catch (error) {
            console.error(`Error fetching data for year ${year}:`, error);
        }
    }
};

scrounge();
