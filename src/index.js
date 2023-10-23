import {hello} from './js/components.js'
import "./styles.css";
import img from './img/webpack.png';


const name = 'Dennys';

const image = new Image();
image.src = img;
document.body.appendChild(image);

console.log(name);
hello(name);