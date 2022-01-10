<template>
  <div class="image-train">
    <div class="row">
      <div class="col-md-2"></div>
      <div class="col-md-6">
        <div class="card">
          <div class="card-header">
            <h5 class="card-title">Prueba de convolución</h5>
          </div>
          <div class="card-body">
            <form>
              <div class="mb-3">
                <label for="formFileSm" class="form-label"
                  >sube una imagen para probar el entrenamiento</label
                >
                <input
                  class="form-control form-control-sm"
                  id="formFileSm"
                  type="file"
                />
              </div>
              <button type="submit" class="btn btn-outline-secondary">Submit</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
.image-train {
  padding-top: 30px;
}
</style>
