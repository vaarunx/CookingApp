document.getElementById("addNewIngredientButton").onclick = function() {
	var IngredientClass = document.getElementById("IngredientClass");
	var input = document.createElement("input");
	input.type = "text";
	var br = document.createElement("br");
    IngredientClass.appendChild(input);
    IngredientClass.appendChild(br);
}