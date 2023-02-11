const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
const tooltipList = [...tooltipTriggerList].map((tooltipTriggerEl) => new bootstrap.Tooltip(tooltipTriggerEl));

function displayConfirm() {
    Swal.fire({
        title: "Successfully Submitted",
        text: "Submitted Content to our Dictionary",
        icon: "success",
    });
}
