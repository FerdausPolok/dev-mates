let totalMinutes = 0;
let countdownInterval;

function updateTimeDisplay(minutes, seconds) {
  const hours = Math.floor(minutes / 60);
  const displayMinutes = minutes % 60;
  const timeDisplay = document.getElementById('time-display');
  timeDisplay.textContent = `${hours}:${displayMinutes < 10 ? '0' : ''}${displayMinutes}:${seconds < 10 ? '0' : ''}${seconds}`;
  console.log(`Time Display Updated: ${hours}h ${displayMinutes}m ${seconds}s`);
}

function startCountdown(totalSeconds) {
  clearInterval(countdownInterval);
  countdownInterval = setInterval(() => {
    if (totalSeconds <= 0) {
      clearInterval(countdownInterval);
      return;
    }
    totalSeconds--;
    const minutes = Math.floor(totalSeconds / 60);
    const seconds = totalSeconds % 60;
    updateTimeDisplay(minutes, seconds);
  }, 1000);
}

document.getElementById('increase').addEventListener('click', () => {
  totalMinutes++;
  updateTimeDisplay(totalMinutes, 0);
});

document.getElementById('decrease').addEventListener('click', () => {
  if (totalMinutes > 0) {
    totalMinutes--;
    updateTimeDisplay(totalMinutes, 0);
  }
});

document.getElementById('start').addEventListener('click', () => {
  console.log('Start button clicked');
  if (totalMinutes <= 0) {
    alert('Please set a valid timer.');
    return;
  }

  chrome.storage.local.set({ timerMinutes: totalMinutes }, () => {
    chrome.runtime.sendMessage({ action: 'startTimer' });

    // Get remaining time from the background script
    chrome.runtime.sendMessage({ action: 'getRemainingTime' }, (response) => {
      if (response && response.remainingTime) {
        const totalSeconds = Math.floor(response.remainingTime / 1000);
        startCountdown(totalSeconds);
      }
    });
  });
});

// Initialize display with time from storage if available
chrome.runtime.sendMessage({ action: 'getRemainingTime' }, (response) => {
  if (response && response.remainingTime) {
    const totalSeconds = Math.floor(response.remainingTime / 1000);
    startCountdown(totalSeconds);
  } else {
    updateTimeDisplay(totalMinutes, 0);
  }
});
