document.addEventListener('DOMContentLoaded', function() {
    const countdownNumberElement = document.getElementById('countdown-number');
    const userInputDate = localStorage.getItem('userInputDate'); // Assuming the date is stored in localStorage

    if (userInputDate) {
        const inputDate = new Date(userInputDate);
        const currentDate = new Date();
        const timeDifference = currentDate - inputDate;
        const daysDifference = Math.floor(timeDifference / (1000 * 60 * 60 * 24));

        countdownNumberElement.textContent = daysDifference;
    } else {
        countdownNumberElement.innerHTML = '<div class="icon calculator-icon"></div>';
    }
});

function navigateTo(slideId) {
    document.querySelectorAll('.slide').forEach(slide => {
        slide.classList.remove('active');
    });
    document.getElementById(slideId).classList.add('active');
}

// Start on the first slide
navigateTo('slide-1');
