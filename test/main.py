# from playwright.sync_api import sync_playwright
import json
import requests
from random import choice

# def web_scrape(url: str):
#     data = {}
#     with sync_playwright() as p:
#         browser = p.chromium.launch()
#         page = browser.new_page()
#         page.goto(url)
        
#         data['title'] = page.title()
        
#         return data

# data = web_scrape('https://pokemondb.net/pokedex/bulbasaur')


philosophers = ['Adam Smith', 'Albert Camus', 'Anaximander', 'Angela Davis', 'Anna Julia Cooper', 'Anne Conway', 'Aristotle', 'Arthur Schopenhauer', 'Auguste Comte', 'Augustine of Hippo', 'Ayn Rand', 'Baruch Spinoza', 'bell hooks', 'Bertrand Russell', 'Betty Friedan', 'Carl Jung', 'Cicero', 'Damaris Cudworth Masham', 'Dante Alighieri', 'David Hume', 'Denis Diderot', 'Diogenes', 'Edmund Burke', 'Edmund Husserl', 'Edward Said', 'Elizabeth Anscombe', 'Emma Goldman', 'Epicurus', 'Francis Bacon', 'Francis Fukuyama', 'Frantz Fanon', 'Friedrich Hayek', 'Friedrich Nietzsche', 'George Berkeley', 'Georges Bataille', 'Georg Wilhelm Friedrich Hegel', 'Giambattista Vico', 'Gilles Deleuze', 'Gottfried Wilhelm Leibniz', 'Guy Debord', 'Hannah Arendt', 'Henri Bergson', 'Henry David Thoreau', 'Heraclitus', 'Herbert Marcuse', 'Herbert Spencer', 'Immanuel Kant', 'Jacques Derrida', 'Jacques Lacan', 'Jane Addams', 'Jean Baudrillard', 'Jean-François Lyotard', 'Jean-Jacques Rousseau', 'Jean-Paul Sartre', 'Jeremy Bentham', 'Johann Gottlieb Fichte', 'John Dewey', 'John Locke', 'John Rawls', 'John Stuart Mill', 'Judith Butler', 'Karl Marx', 'Karl Popper', 'Leo Strauss', 'Louis Althusser', 'Luce Irigaray', 'Ludwig Wittgenstein', 'Marcus Aurelius', 'Marshall McLuhan', 'Martin Heidegger', 'Mary Wollstonecraft', 'Maurice Merleau-Ponty', 'Max Weber', 'Michel de Montaigne', 'Michel Foucault', 'Montesquieu', 'Niccolò Machiavelli', 'Noam Chomsky', 'Parmenides', 'Peter Singer', 'Pierre-Joseph Proudhon', 'Plato', 'Plotinus', 'Protagoras', 'Pythagoras', 'Ralph Waldo Emerson', 'René Descartes', 'Richard Rorty', 'Robert Nozick', 'Roger Bacon', 'Roland Barthes', 'Rosa Luxemburg', 'Seneca', 'Sigmund Freud', 'Simone de Beauvoir', 'Slavoj Žižek', 'Socrates', 'Sojourner Truth', 'Søren Kierkegaard', 'Susan Sontag', 'Thales of Miletus', 'Theodor W. Adorno', 'Thomas Aquinas', 'Thomas Hobbes', 'Thomas Kuhn', 'Thomas Nagel', 'Voltaire', 'Walter Benjamin', 'W. E. B. Du Bois', 'Wilhelm von Humboldt', 'William James', 'William of Ockham', 'Xenophanes', 'Zeno']
data = requests.get(f'https://philoapi.vercel.app/search?keyword={choice(philosophers)}').json()
with open('test/data.json', 'w') as f:
    json.dump(data, f)