function clearScreen() {
    document.getElementById("output").value = "";
}
function display(value) {
    document.getElementById("output").value += value;
}

function calculate() {
    var x = document.getElementById("output").value;
    var y = eval(x);
    document.getElementById("output").value = y;
}