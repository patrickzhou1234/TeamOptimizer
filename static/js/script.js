const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
const tooltipList = [...tooltipTriggerList].map((tooltipTriggerEl) => new bootstrap.Tooltip(tooltipTriggerEl));

function displayConfirm() {
    Swal.fire({
        title: "Successfully Submitted",
        text: "Submitted Content to our Dictionary",
        icon: "success",
    });
}

function displayComputed() {
    Swal.fire({
        title: "Successfully Submitted",
        text: "Submitted Content to our Servers",
        icon: "success",
    });
}

function clearContent() {
    Swal.fire({
        title: "Successfully Cleared",
        text: "Successfully Cleared Server Contents",
        icon: "success",
    });
}
