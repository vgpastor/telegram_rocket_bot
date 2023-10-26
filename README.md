# Telegram Rocket Launch Bot

Technical test for WithMadrid.

## Tech choices
Use of python-telegram-bot because it's a modern and well maintained library. It's also very easy to use and has a lot of features.

The structure it's based in hexagonal architecture to separate the business logic from the infrastructure. This way we can change the infrastructure without changing the business logic.This way we can change the infrastructure without changing the business logic.

The abstraction layer provide a domain model that can be used by any other infrastructure. In this case we have a telegram implementation but we can have a web implementation or a CLI implementation.

## To do
- Improve the test coverage
- Add a CI/CD pipeline
- Add terraform to the infra deployment
- Improve business logic and show the result to the user.
- Improve bisection algorith to contemplate the fails of the user.
- Reuse the same telegram message to make more user friendly the bot.

