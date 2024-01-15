function uploadFile() {
    const fileInput = document.getElementById('fileInput');
    const loadingDiv = document.getElementById('loading');
    const resultDiv = document.getElementById('result');
    const textSummary = document.getElementById('textSummary');
    const audioSummary = document.getElementById('audioSummary');

    loadingDiv.style.display = 'block';

    // Simulate backend request (replace this with actual backend integration)
    setTimeout(() => {
        // Assuming backend returns summary as text and audio URL
        const summaryText = "This is a sample summary text.";
        const audioUrl = "path/to/summary/audio.mp3";

        loadingDiv.style.display = 'none';
        resultDiv.style.display = 'block';

        textSummary.innerText = summaryText;
        audioSummary.src = audioUrl;
        audioSummary.classList.remove('hidden');
    }, 2000); // Simulating a 2-second backend processing time
}
