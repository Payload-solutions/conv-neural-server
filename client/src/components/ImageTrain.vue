<template>
  <div class="image-train">
    <div class="row">
      <div class="col-md-1"></div>
      <div class="col-md-5">
        <div class="card">
          <div class="card-header">
            <h5 class="card-title">Prueba de convolución</h5>
          </div>
          <div class="card-body">
            <form @submit.prevent="sendImage">
              <div class="mb-3">
                <label for="formFileSm" class="form-label"
                  >sube una imagen para probar el entrenamiento</label
                >
                <input
                  class="form-control form-control-sm"
                  name="formImageFiles"
                  @change="onChange"
                  type="file"
                  required
                />
              </div>
              <button type="submit" class="btn btn-outline-secondary">
                <img src="../assets/arrow.png" alt="" /> probar
              </button>
            </form>
          </div>
        </div>
      </div>
      <div class="col-md-5">
        <Metrics/>
      </div>
      <div class="col-md-1"></div>
      <div class="col-md-1"></div>
      <div id="modal-container" class="col-md-5">
        <div>
          <b-button
            v-show="convolution.length > 0"
            v-b-toggle.collapse-1
            variant="success"
            >Toggle Collapse</b-button
          >
          <b-collapse id="collapse-1" class="mt-2">
            <b-card>
              <p class="card-text">Clasificación del yogur</p>
              <b-button v-b-toggle.collapse-1-inner size="sm"
                >métricas</b-button
              >
              <b-collapse
                v-bind:key="index"
                v-for="(item, key, index) in convolution[0]"
                id="collapse-1-inner"
                class="mt-2"
              >
                <b-card>{{ key }} - {{ item }}</b-card>
              </b-collapse>
            </b-card>
            <b-button
              v-b-toggle.collapse-1
              variant="warning"
              @click="reloadPage"
              >reiniciar convolución</b-button
            >
          </b-collapse>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Metrics from '../containers/Metrics.vue';
export default {
  name: "ImageTrain",
  props: ["imageTrain"],
  data() {
    return {
      values: [],
      convolution: [],
      imageData: null,
    };
  },
  created() {},
  methods: {
    onChange(event) {
      this.imageData = event.target.files[0];
    },
    sendImage() {
      const formData = new FormData();
      formData.append("formImageFiles", this.imageData, this.imageData.name);
      axios
        .post("http://localhost:5000/train", formData, {
          headers: {
            Accept: "application/json",
            "Content-type": "application/json",
          },
        })
        .then((response) => {
          this.convolution.push(response.data.content);
          console.log(this.convolution);
        });
    },
    reloadPage() {
      window.location.reload();
    },
  },
  components:{
      Metrics
  }
};
</script>

<style>
.image-train {
  padding-top: 30px;
  margin-right: 30px;
}

#modal-container {
  padding-top: 20px;
}
</style>

