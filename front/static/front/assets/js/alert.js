htmx.on('htmx:responseError', function(evt) {
    Swal.fire({
        icon: 'error',
        title: "Echec de la demande",
        text: evt.detail.xhr.responseText,
        showConfirmButton: false,
        timer: 5000
    })
});

htmx.on("ContactSuccess", function() {
    Swal.fire({
        icon: 'success',
        title: "Demande réussite",
        text: "Vôtre demande a bien été envoyé",
        showConfirmButton: false,
        timer: 3000
    })
});


