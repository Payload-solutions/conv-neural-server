5 lines (5 sloc)  89 Bytes
<template>
  <div class="about">
    <div class="row">
      <div id="info1" class="col-md-8">
        <div class="card">
          <div class="card-header">
              <h5 class="card-title">¿Qué es una Red Convolucional?</h5>
          </div>
          <div class="card-body">
            <p class="card-content">
              Es una red neuronal que está especializadas en la detección y manejo de imágenes; directamente
              especializadas en simular la corteza visual del cerebro.
            </p>
            <img src="../assets/conv-full-layer.gif" class="img-fluid" alt="">
          </div>
        </div>
      </div>
      <div id="info1" class="col-md-6">
        <div class="card">
          <div class="card-header">
              <h5 class="card-title">Pero ¿cómo vemos los humanos?</h5>
          </div>
          <div class="card-body">
            <p class="card-content">
              Los humanos vemos y reconocemos imágenes diferentes basándonos en los patrones que nuestro cerebro interpreta.
            </p>
            <img src="../assets/image-conv.gif" class="img-fluid" alt="">
          </div>
        </div>
      </div>
      <div id="info1" class="col-md-4">
        <div class="card">
          <div class="card-header">
              <h5 class="card-title">¿Qué es una Red Convolucional?</h5>
          </div>
          <div class="card-body">
            <p class="card-content">
              Una red convolucional, trata de imitar el comportamiento de la corteza cerebral.
            </p>
            <img src="../assets/conv-full-layer.gif" class="img-fluid" alt="">
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<style>
  .about{
    padding-top: 30px;
    margin-right: 20px;
  }
  #info1{
    padding-left: 50px;
  }
</style>