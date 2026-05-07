async function generateContent() {

    const product = document.getElementById('product').value;
    const audience = document.getElementById('audience').value;
    const tone = document.getElementById('tone').value;
    const platform = document.getElementById('platform').value;
    const content_type = document.getElementById('content_type').value;

    document.getElementById('output').innerHTML =
        "Generating AI storytelling content...";

    const response = await fetch('/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },

        body: JSON.stringify({
            product,
            audience,
            tone,
            platform,
            content_type
        })
    });

    const data = await response.json();

    document.getElementById('output').innerHTML = data.result;
}