htmx.on('htmx:responseError', function(evt) {
    Swal.fire({
        icon: 'error',
        title: "Echec de la demande",
        text: evt.detail.xhr.responseText,
        showConfirmButton: false,
        timer: 5000
    })
});


