document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("login_button").addEventListener("click", function () {
        window.location.href = "{% url 'login' %}";
    });
    document.getElementById("write_button").addEventListener("click", function () {
        window.location.href = "{% url 'write' %}";
    });
});