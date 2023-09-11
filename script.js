// Replace with your GitHub username
const githubUsername = "itsayopapi";

// Function to fetch GitHub repositories
async function fetchGitHubRepos(username) {
    const response = await fetch(`https://api.github.com/users/${username}/repos`);
    const data = await response.json();
    return data;
}

// Function to display repositories
function displayRepos(repositories) {
    const projectsContainer = document.getElementById("projects");

    repositories.forEach(repo => {
        const repoCard = document.createElement("div");
        repoCard.classList.add("card");

        const repoName = document.createElement("h2");
        repoName.textContent = repo.name;

        const repoDescription = document.createElement("p");
        repoDescription.textContent = repo.description;

        const repoLink = document.createElement("a");
        repoLink.href = repo.html_url;
        repoLink.textContent = "View on GitHub";

        repoCard.appendChild(repoName);
        repoCard.appendChild(repoDescription);
        repoCard.appendChild(repoLink);

        projectsContainer.appendChild(repoCard);
    });
}

// Fetch and display GitHub repositories on page load
window.addEventListener("load", async () => {
    const repositories = await fetchGitHubRepos(githubUsername);
    displayRepos(repositories);
});
