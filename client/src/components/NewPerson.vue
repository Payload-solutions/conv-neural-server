
<template>
  <div id="main">
    <div class="container">
      <div class="row pt-5">
        <div class="col-md-5">
          <div class="card">
            <div class="card-body">
              <form @submit.prevent="addPerson(persona.personCode,
              persona.personaName,persona.personBirth,zonas,persona.codeZone,
              persona.personSalary)">
                <div class="form-group">
                  <input v-model="persona.personCode" required type="text" placeholder="cedula" class="form-control">
                </div>
                <div class="form-group">
                  <input v-model="persona.personaName" required type="text" placeholder="Nombre" class="form-control">
                </div>
                <div class="form-group">
                  <input v-model="persona.personBirth" required type="date"  class="form-control">
                </div>
                <div class="form-group">
                  <select v-model="persona.codeZone"    class="form-control">
                    <option v-bind:key="zona.id" v-for="zona in zonas" >{{zona.zoneCode}}</option>
                  </select>
                </div>
                <div class="form-group">
                  <input v-model="persona.personSalary" required type="number" placeholder="sueldo" min="0"  class="form-control">
                </div>
                <button type="submit" class="btn btn-block btn-success">Agregar</button>
              </form>
            </div>
          </div>
        </div>
        <div class="col-md-7">
          <table class="table table-striped">
            <thead>
              <tr>
                 <th scope="col">Accion</th>
                <th scope="col">Codigo de persona</th>
                <th scope="col">Nombres</th>
                <th scope="col">Año de nacimiento</th>
                <th scope="col">Sueldo</th>
              </tr>
            </thead>
            <tbody v-bind:key="persona.id" v-for="persona in personas">
              <tr>
                <td><b-button
                    @click="
                      deletePerson(
                        persona.personCode,
                        persona.personName,
                        persona.personBirth,
                        persona.personSalary
                      )
                    "
                    variant="danger"
                    >delete</b-button
                  ></td>
                <td>
                  
                  {{ persona.personCode }}
                </td>
                <td>{{ persona.personName }}</td>
                <td>{{ persona.personBirth }}</td>
                <td>{{ persona.personSalary }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import moment from'moment';
export default {
  name: "PersonaValues",
  props: ["personas"],
  data() {
    return {
      person: {
        personCode: "",
        personaName: "",
        personBirth: "",
        personSalary: "",
      },
      zonas:[],
      sectores:[],
      persona:{
        personCode: "",
        personaName: "",
        personBirth: "",
        personSalary: "",
        zone:{
            zoneCode: "",
            zoneDescription: "",
            sector: {
                sectorCode: "",
                sectorDescription: ""
            }
        },
        sector: {
            sectorCode: "",
            sectorDescription: "",
        }
      }
    };
  },
  created(){
    this.loadZonas();
  },
  methods: {
    deletePerson(code, names, birth, salary) {
      console.log(code, names, birth, salary);
      fetch("http://localhost:8082/deletePerson", {
        method: "DELETE",
        body: JSON.stringify({
          personCode: code,
          personName: names,
          personBirth: birth,
          personSalary: salary,
        }),
        headers: {
          Accept: "application/json",
          "Content-type": "application/json",
        },
      })
        .then((res) => res.json())
        .then((data) => console.log(data));
    },
    /**
     * person.personCode,
              person.personaName,person.personBirth,zona.zoneCode, zona.zoneDescription,
               zona.sector.sectorCode, zona.sector.sectorDescription,person.personSalary
     */
    addPerson(code, name, birth, zonas, codeZone, salary){
      let sectorCode = "";
      let sectorDescription = "";
      let zoneDescription ="";
      console.log(code, name, birth,zonas, codeZone, salary);
      zonas.forEach(element => {
          if (element.zoneCode === codeZone){
              zoneDescription = element.zoneDescription;
              sectorCode = element.sector.sectorCode;
              sectorDescription = element.sector.sectorDescription;
          }
      });
      fetch("http://localhost:8082/insertPersons", {
        method: "POST",
        body: JSON.stringify({
        personCode:code ,
        personName:name ,
        personBirth:moment(String(birth)).format('MM/DD/YYYY hh:mm'),
        zone: {
            zoneCode:codeZone ,
            zoneDescription: zoneDescription,
            sector: {
                sectorCode:sectorCode ,
                sectorDescription:sectorDescription 
            }
        },
            sector:  {
                sectorCode:sectorCode ,
                sectorDescription:sectorDescription 
            },
        personSalary: salary
    }),
        headers: {
          Accept: "application/json",
          "Content-type": "application/json",
        },
      })
        .then((res) => res.json())
        .then((data) => console.log(data));
    }
    ,
    loadSectores(){
      fetch('http://localhost:8082/sector/getSectors')
    },
    loadZonas(){
      fetch('http://localhost:8082/zone/getZones')
        .then(res => res.json())
        .then(data => {
          this.zonas = data;
          console.log(this.zonas[0].sector.sectorDescription);
        })
    }
  },
};
</script>
>

<style>
#main {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  font-size: 16px;
  margin-left: -10px;
}
</style>