document.addEventListener('DOMContentLoaded', function () {
    const formulario = document.getElementById('formulario-busqueda');
    const cargando = document.getElementById('cargando');

    if (formulario && cargando) {
        formulario.addEventListener('submit', function () {
            if (formulario.checkValidity()) {
                cargando.style.display = 'flex';
            }
        });
    }
});
