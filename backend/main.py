from fastapi import FastAPI
from api.v1 import recipes, ingredients, ai_interactions  # Import your new AI route

app = FastAPI()

# Register API routes
#app.include_router(recipes.router, prefix="/v1")
#app.include_router(ingredients.router, prefix="/v1")
app.include_router(ai_interactions.router, prefix="/v1")
