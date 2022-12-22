<template>
    <div class="profile">
        <br/>
    
    <div class="row justify-content-center align-items-center" style="min-width: 320px">
        <div class="col-5">
            <br/>
            <div class="border rounded bg-light p-5 ">
                <h1 class="h3 mb-4">Edit Profile</h1>
                <br/>
                <input type="url" id="inputTitle" class="form-control" placeholder="Item Image (Link)" v-model="user.userImage"/>
                <br/>
                <input type="email" id="inputEmail" class="form-control" placeholder="Email address" v-model="user.userEmail"/>
                <br/>
                <input type="date" id="inputDOB" class="form-control" v-model="user.userDateOfBirth"/>
                <br/>
                <div class="d-grid gap-2 col-8 mx-auto">
                    <button class="btn btn-primary" type="submit" @click = "updateUser()">Save Changes</button>
                </div>

            </div>
        </div>
    </div>

</div>
</template>

<script>
    export default{
        name:'Profile',
        data(){
            return{
                //missing UserID
                user:{
                'id':'',
                'username': '',
                'userEmail': '',
                'userDateOfBirth': '',
                'userImage': '',
                'password':'',
                }    
            }
        },
        methods:{
            async updateUser(){
                //await this.getUsers();
                //get the id of the authenticated user
                this.user.id = this.$session.get('user_id')
                await fetch(`http://127.0.0.1:8000/api/users/${this.user.id}/`,{
                method: 'put',
                headers: {
                'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.user)  
                });
                //await this.getUsers();
                this.user = {};
            },
            
            // 
        }
    }
</script>