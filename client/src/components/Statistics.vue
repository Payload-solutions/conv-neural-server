<template>
    <div class="statistics">

    </div>
</template>

<script>
    import axios from 'axios';
    export default{
        name:"Statistic",
        props: ["statistic"],
        data (){
            return {
                values: {}
            }
        },
        created(){
            this.loadHistory();
        },
        methods:{
            loadHistory(){

                axios.get("http://127.0.0.1:5000/about-model")
                    .then((res) => {
                        this.values = res.data;
                        console.log(this.values);
                    })
                    .catch((error)=>{
                        console.log(error);
                    })
            }
        }
    }
</script>
