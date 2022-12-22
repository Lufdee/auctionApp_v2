<template>
     <div class="row justify-content-center" style="min-width: 320px; min-height: 100vh; margin-top: 3rem;">
        <div class="col-10 col-md-8 col-lg-8">
            <div class="border rounded bg-light shadow p-5">
                <form @submit.prevent="addAuction">
                    <h1 class="h3 mb-4">New Item</h1>
                    <br/>
                    <input type="text" id="inputTitle" class="form-control" placeholder="Title" v-model="newAuction.itemTitle"/>
                    <br/>
                    <textarea id="inputDescription" class="form-control" placeholder="Item Description" v-model="newAuction.itemDescription"/>
                    <br/>
                    <input type="url" id="inputTitle" class="form-control" placeholder="Item Image (Link)" v-model="newAuction.itemPicture"/>
                    <br/>
                    <input type="date" id="inputEnd" class="form-control" required v-model="newAuction.itemFinishDate"/>
                    <br/>
                    <input type="number" id="inputStartPrice" class="form-control" placeholder="Starting Price" required v-model="newAuction.itemStartPrice"/>
                    <br/>
                    <div class="d-grid gap-2 col-6 mx-auto">
                        <button class="btn btn-primary" type="submit" @click = "addAuction()">Submit Item</button>
                    </div>     
                </form>
            </div>
        </div>
    </div>
</template>

<script>
    export default{
        name: 'NewItem',
        data(){
            return{
                newAuction:{
                    'itemTitle':'',
                    'itemDescription':'',
                    'itemStartPrice':'',
                    'itemPicture': '',
                    'itemFinishDate':'',
                    'ownerId':'',      
                }
            }
        },
        methods:{
        async addAuction(request){
            current_user = request.user
            this.ownerId = current_user.id
            await fetch("http://127.0.0.1:8000/api/auction/",{
          method: 'post',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.newAuction)  
        });
        this.newAuction = {};
        }, 

     } 
        
    }


</script>