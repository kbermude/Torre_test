<template lang="html">
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <h2>Opportunities</h2>
                <div class="col-md-12">
                     <div class="row mt-3">
                    
                        <div class="col-md-4" v-for="opportunity in opportunities" v-bind:key="opportunity.id"> 
                    
                            <div class="card mb-3" style="box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);">
                            <img class="card-img-top img-hover-zoom " v-bind:src="opportunity.picture" v-bind:alt="image">
                            <div class="card-body">
                                <h3 class="card-title mb-3">{{ opportunity.objective }}</h3>
                                <p class="card-text"><strong>Type:</strong> {{ opportunity.type }}</p>
                                <p class="card-text"><strong>Remote:</strong> {{ opportunity.remote }}</p>
                                <p class="card-text"><strong>Company:</strong> {{ opportunity.organizations }}</p>
                                <p class="card-text"><strong>Salary:</strong> $ {{ opportunity.salary }}</p>
                                <!-- <p class="card-text"><strong>Debilidad:</strong> {{ item.debilidad }}</p> -->
                            </div>
                            </div>
                    
                        </div>
                    
                    </div>
                   
                    <!-- <b-table striped hover :items="opportunities" :fields="fields"></b-table> -->
                </div>

            </div>
        </div>
    </div>

</template>
<script>
import axios from 'axios'
export default{
    name:'opportunities',
    data(){
        return{
            fields:[
                // {key:'title', label: 'Title'},
                {key:'id', label: 'Code'},
                {key:'objective', label: 'Opportunity'},
                {key:'type', label: 'Type'},
                {key:'organizations', label: 'Company'},
                {key:'remote', label: 'Remote'},
                {key:'location', label: 'Location'},
                {key:'salary', label: 'Salary'},
                {key:'picture', label: 'Image'}
            ],
            opportunities:[]
        }
    },
    methods:{
        getOpportunities () {
            const path = 'https://search.torre.co/opportunities/_search/?size=12'
            var params = {"skill/role":{
            "text":"Software Engineering",
            "experience": "potential-to-develop"}}
            axios.post(path).then((response) =>{
                console.log(response['data']['results'][0])
                console.log(response['data']['results'][9]['organizations'][0]['name'])
                console.log("Compesation")
                console.log(response['data']['results'][9]['compensation']['data'])
                this.opportunities = response.data.results
                var n = [0,1,2,3,4,5,6,7,8,9,10,11]
                n.forEach(i=>{
                    this.opportunities[i].salary = 0;
                    this.opportunities[i].picture = "";
                      
                    if (response['data']['results'][i]['organizations'].length>=1){ 
                        this.opportunities[i].picture = response['data']['results'][i]['organizations'][0]['picture']  
                        this.opportunities[i].organizations = response['data']['results'][i]['organizations'][0]['name'];
                        
                    }
                    if (response['data']['results'][i]['compensation']['data']!=null && response['data']['results'][i]['compensation']['data']['minAmount']!=null){   
                       this.opportunities[i].salary = response['data']['results'][i]['compensation']['data']['minAmount'];
                    }else{
                        this.opportunities[i].salary = 0;
                    }
                })                
                
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
.img-hover-zoom {
    height: 300px;
    overflow: hidden; 
    background-size:cover;
  }
  
.img-hover-zoom img {
    transition: transform .5s ease;
    background-size:cover;
}
.img-hover-zoom:hover img {
    transform: scale(1.3);
    background-size:cover;
}
</style>
