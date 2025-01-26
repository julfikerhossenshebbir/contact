document.querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault(); // Stop default submission to show alert
    const name = document.querySelector('#name').value;
    alert(`ধন্যবাদ, ${name}! আপনার ফর্মটি জমা দেওয়া হচ্ছে...`);
    this.submit(); // Continue with submission
});
