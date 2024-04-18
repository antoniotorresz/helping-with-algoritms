function array(lst, idx){
    return (lst.length <= idx || idx < 0) ? "Elemento no válido" : lst[idx];
}
let number = array([1, 2, 3, 4, 5], 3);
console.log(number);