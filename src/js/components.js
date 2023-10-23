import '../css/components.css';

export const hello = (name) => { 
    console.log('Cargando etiqueta');

    const h1 = document.createElement('h1');

    h1.innerHTML = `hola ${name}, Bienvenido!`;

    document.body.append(h1);
};