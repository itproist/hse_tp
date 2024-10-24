const inputIngredient = document.getElementById('input-ingredient');
const addButton = document.getElementById('add-button');
const removeButton = document.getElementById('remove-button');
const ingredientList = document.getElementById('ingredient-list');
let ingredients = [];

addButton.addEventListener('click', () => {
  const ingredient = inputIngredient.value.trim();

  if (ingredient !== '') {
    ingredients.push(ingredient); //добавляем
    updateIngredientList();
    inputIngredient.value = ''; //очищаем текст который чел написал и значение
  }
});
// обновляем 
function updateIngredientList() {
  ingredientList.textContent = ''; 
  
  if (ingredients.length > 0) {
    ingredientList.textContent = ingredients.join(', ');
  }
// а это для удаления
}
removeButton.addEventListener('click', () => {
    if (ingredients.length > 0) {
      ingredients.pop();
      updateIngredientList();
    }
  });