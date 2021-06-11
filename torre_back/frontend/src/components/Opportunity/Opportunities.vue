<template lang="html">
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <h2>Opportunities List</h2>
                <div class="col-md-12">
                    <b-table striped hover :items="opportunities" :fields="fields">

                    </b-table>
                </div>

            </div>
        </div>
    </div>

</template>
<script>
import axios from 'axios'
export default{
    data(){
        return{
            fields:[
                // {key:'title', label: 'Title'},
                // {key:'code', label: 'Code'},
                {key:'objective', label: 'Opportunity'},
                {key:'type', label: 'Type'},
                //{key:'organizations', label: 'Company'},
                {key:'remote', label: 'Remote'},
                {key:'location', label: 'Location'},
                {key:'salary', label: 'Salary'}
            ],
            opportunities:[]
        }
    },
    methods:{
        getOpportunities () {
            const path = 'https://search.torre.co/opportunities/_search/?size=10'
            axios.post(path).then((response) =>{
                console.log(response['data']['results'][0])
                //console.log(response['data']['results']['organizations'])
                console.log(response['data']['results'][0]['compensation']['data']['minAmount'])
                this.opportunities = response.data.results
                //this.opportunities.organizations = response.data.results.organizations[0].name
                this.response.forEach(data =>{
                    data.results.forEach(compensation=>{
                        

                    })

                })
                for (i in this.opportunities){
                    this.opportunities.salary = response['data']['results'][i]['compensation']['data']['minAmount']
                }
                
            })
            .catch((error)=>{
                console.log(error)
            })
        }
    },
    created(){
        this.getOpportunities()
    }
}
</script>
<style lang="css" scoped>

</style>
