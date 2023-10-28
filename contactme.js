window.onload = function() {
    document.getElementById('contact-form').addEventListener('submit', function(event) {
        event.preventDefault();
        // generate a five digit number for the contact_number variable
        this.contact_number.value = Math.random() * 100000 | 0;
        // these IDs from the previous steps
        emailjs.sendForm('service_3koo0h9', 'contact_form', this)
            .then(function(response) {
                console.log('SUCCESS!', response.status, response.text);
                alert("Email sent! Thanks for your message.")
            }, function(error) {
                console.log('FAILED...', error);
                alert("Email failed to send. Please try again.")
            });
    });
}

function reset_form() {
    $("#contact-form")[0].reset();
}