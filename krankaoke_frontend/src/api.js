import axios from "axios";
// Figure out why config does not work
const config = new Map();

class Api {
  constructor(baseUrl, apiUser, apiPassword) {
    this.baseUrl = baseUrl == undefined ? config.get("api.baseUrl") : baseUrl;
    this.apiUser = apiUser == undefined ? config.get("api.user") : apiUser;
    this.apiPassword =
      apiPassword == undefined ? config.get("api.password") : apiPassword;
    this.accessToken = undefined;
    this.userId = undefined;
    this.client = undefined;
  }

  getApiToken() {
    return axios
      .post("http://localhost:8080/api_token/", {
        username: this.apiUser,
        password: this.apiPassword
      })
      .then(response => {
        if (response.status == 200) {
          let payload = response.data;
          this.accessToken = payload["token"];
          this.client = axios.create({
            headers: { Authorization: "Token " + this.accessToken },
            timeout: 3000,
            baseURL: "http://localhost:8080/api/v1/"
          });
          return payload["token"];
        } else {
          alert(response);
        }
      })
      .catch(() => alert("Something went wrong while getting API token"));
  }

  getUserMetadata() {
    return this.client({
      url: "/users/me/",
      method: "get"
    })
      .then(response => {
        if (response.status == 200) {
          let payload = response.data;
          this.userId = payload["id"];
        } else {
          alert(response);
        }
      })
      .catch(() => alert("Something went wrong while getting user metadata"));
  }

  async initialize() {
    await this.getApiToken().then(() => this.getUserMetadata());
  }

  async krankaokes() {
    return await this.client({
      url: "/krankaokes/",
      method: "get"
    })
      .then(response => {
        if (response.status == 200) {
          return response.data["results"];
        } else {
          alert("Failed to fetch Krankaokes", response);
        }
      })
      .catch(e => alert(e));
  }

  async createKrankaoke(form) {
    let data = new FormData();
    data.append("audio", form.audio);
    data.append("artist", form.artist);
    data.append("title", form.title);
    data.append("user", form.user);

    return this.client({
      url: "/krankaokes/",
      method: "post",
      data: data,
      headers: { "Content-Type": "multipart/form-data" }
    });
  }

  async getKrankaoke(id) {
    return await this.client({
      url: "/krankaokes/" + id + "/",
      method: "get"
    })
      .then(response => {
        if (response.status == 200) {
          return response.data;
        } else {
          alert("Failure while getting krankaoke with id: " + id);
        }
      })
      .catch(() => alert("Error while getting krankaoke with id: " + id));
  }
}

const api = new Api("http://localhost:8080/", "test", "test");
export default api;
