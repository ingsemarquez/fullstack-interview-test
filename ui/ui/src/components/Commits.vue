<template>
  <div id="commit">
    <h1>List of Commits</h1>
    <div>
      <ul v-if="commits && commits.length">
        <li v-for="commit of commits">
          <p>{{ commit.name }}</p>
        </li>
      </ul>

      <ul v-if="errors && errors.length">
        <li v-for="error of errors">
          <p>{{ error }}</p>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      commits: [],
      errors: [],
    };
  },
  async created() {
    try {
      this.commits = await axios.get("http://localhost:8000/commits_by_branch/");
    } catch (error) {
      this.errors.push(error);
    }
  },
};
</script>

<style>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  top: -10px;
}
</style>
