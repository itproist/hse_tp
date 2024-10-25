const inputIngredient = document.getElementById('input-ingredient');
const addButton = document.getElementById('add-button');
const removeButton = document.getElementById('remove-button'); 
const sendButton = document.getElementById('send-button'); // Кнопка отправки
const ingredientList = document.getElementById('ingredient-list');
const recipesDiv = document.getElementById('recipes'); // Добавляем div для вывода рецептов
let ingredients = [];

addButton.addEventListener('click', () => {
  const ingredient = inputIngredient.value.trim();

  if (ingredient !== '') {
    ingredients.push(ingredient);
    updateIngredientList();
    inputIngredient.value = ''; 
  }
});

removeButton.addEventListener('click', () => { 
  if (ingredients.length > 0) {
    ingredients.pop(); 
    updateIngredientList();
  }
});

sendButton.addEventListener('click', () => { // Обработчик для кнопки "Отправить"
  fetch('/api/recipy', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(ingredients) // Отправляем массив ингредиентов
  })
  .then(response => response.json())
  .then(data => {
    displayRecipes(data); // Выводим полученные рецепты
  })
  .catch(error => {
    console.error('Ошибка при получении рецептов:', error);
  });
});

function updateIngredientList() {
  ingredientList.textContent = '';

  if (ingredients.length > 0) {
    ingredientList.textContent = ingredients.join(', ');
  }
}

function displayRecipes(recipes) { // Функция для вывода рецептов
  recipesDiv.textContent = ''; // Очищаем предыдущие рецепты

  if (recipes.length > 0) {
    const recipeList = document.createElement('ul');
    for (const recipe of recipes) {
      const listItem = document.createElement('li');
      listItem.textContent = `${recipe.name}: ${recipe.recipe}`;
      recipeList.appendChild(listItem);
    }
    recipesDiv.appendChild(recipeList);
  } else {
    recipesDiv.textContent = 'Рецептов не найдено.';
  }
}
