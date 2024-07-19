// ==UserScript==
// @name         网页自动复制URL
// @namespace    http://tampermonkey.net/
// @version      1.0
// @description  Create a fixed button on YouTube to copy the current page URL to clipboard and run a Windows program
// @author       Your Name
// @match        *://*.youtube.com/*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=YouTube.com
// @grant        GM_addStyle
// @grant        GM_xmlhttpRequest
// @require      https://cdnjs.cloudflare.com/ajax/libs/clipboard.js/2.0.6/clipboard.min.js
// ==/UserScript==

(function() {
    'use strict';

    // Create a button
    var button = document.createElement('button');
    button.innerHTML = '本地下载';
    button.style.position = 'fixed';
    button.style.top = '63.9953px';
    button.style.left = '23.9953px';
    button.style.zIndex = '1000';
    button.style.backgroundColor = 'rgba(255, 255, 255, 0.20)'; // White with 20% opacity
    button.style.color = 'white';
    button.style.border = 'none';
    button.style.borderRadius = '25px'; // Makes the button elliptical
    button.style.padding = '5px 10px'; // Adjust padding for size
    button.style.cursor = 'pointer';
    button.style.fontSize = '16px';
    button.style.fontWeight = 'bold';
    button.style.textAlign = 'center';
    button.style.boxShadow = '0px 4px 6px rgba(0,0,0,0.1)'; // Optional shadow for better visibility
    document.body.appendChild(button);

    // Create a hidden input to use for copying URL
    var input = document.createElement('input');
    input.style.position = 'absolute';
    input.style.left = '-9999px'; // Hide the input
    document.body.appendChild(input);

    document.body.appendChild(button);

    // Initialize Clipboard.js with the button
    var clipboard = new ClipboardJS(button, {
        text: function() {
            var pageUrl = window.location.href; // Get the current page URL
            input.value = pageUrl; // Set input value to current page URL
            input.select(); // Select the input value
            return pageUrl; // Return the value to be copied
        }
    });

    clipboard.on('success', function(e) {
        console.log('URL copied to clipboard:', e.text);
        e.clearSelection();

        // Run the local server to execute the batch file
        fetch('http://localhost:5000/run-program', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ command: 'D:\\YDODS\\youtube.bat' })
        })
        .then(response => response.json())
        .then(data => {
            console.log('Program executed:', data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });

    clipboard.on('error', function(e) {
        console.error('Failed to copy URL:', e);
    });
})();
