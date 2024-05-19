const data = {
  email: "kieran@example.com",
  username: "kieran",
  full_name: "string",
  password: "password",
};

async function postData(url = "", data = {}) {
  const response = await fetch(url, {
    method: "POST",
    mode: "cors",
    cache: "no-cache",
    credentials: "same-origin",
    headers: {
      "Content-Type": "application/json",
    },
    redirect: "follow",
    referrerPolicy: "no-referrer",
    body: JSON.stringify(data),
  });

  return response.json();
}

const username = "kieran";
const password = "password";

async function postFormData(url = "", data = {}) {
  const formData = new URLSearchParams();
  for (const key in data) {
    formData.append(key, data[key]);
  }

  const response = await fetch(url, {
    method: "POST",
    mode: "cors",
    cache: "no-cache",
    credentials: "same-origin",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    redirect: "follow",
    referrerPolicy: "no-referrer",
    body: formData,
  });

  return response.json();
}

const accessToken =
  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJraWVyYW4iLCJleHAiOjE3MTYxMTExNDh9.OpWi-IG6cM46nEuK7ttw-yPq_TwecM8HEmNsoAlwNQE";

async function getUsers(url = "", token) {
  const response = await fetch(url, {
    method: "GET",
    mode: "cors",
    cache: "no-cache",
    credentials: "same-origin",
    headers: {
      Authorization: `Bearer ${token}`,
      "Content-Type": "application/json",
    },
    redirect: "follow",
    referrerPolicy: "no-referrer",
  });

  return response.json();
}

postData("http://0.0.0.0:8000/api/users", data)
  .then((data) => {
    console.log(data);
  })
  .catch((error) => {
    console.error("Error:", error);
  });

// postFormData("http://0.0.0.0:8000/token", {
//   username: username,
//   password: password,
// })
//   .then((data) => {
//     console.log(data);
//   })
//   .catch((error) => {
//     console.error("Error:", error);
//   });

// getUsers("http://0.0.0.0:8000/api/users", accessToken)
//   .then((data) => {
//     console.log(data);
//   })
//   .catch((error) => {
//     console.error("Error:", error);
//   });
