<template>
  <div id="branch">
    <h1>List of Branches</h1>
    <div>
      <ul v-if="branches && branches.length">
        <li v-for="branch of branches">
          <p>{{ branch.name }}</p>
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
      branches: [],
      errors: [],
    };
  },
  async created() {
    try {
      this.branches = await axios.get("http://localhost:8000/branches");
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
