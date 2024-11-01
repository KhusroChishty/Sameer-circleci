// main.js
fetch('/config.json')
  .then(response => response.json())
  .then(config => {
    const apiUrl = config.apiEndpoint;

    // Example usage in a fetch request
    fetch(`${apiUrl}/endpoint`)
      .then(response => response.json())
      .then(data => console.log(data));
  })
  .catch(error => console.error('Error loading config:', error));
