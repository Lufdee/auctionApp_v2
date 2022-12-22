<template>
  <Navbar/>
  <router-view :key="$route.path" />
</template>

<script>
import Profile from './components/Profile.vue'
import Home from './components/Home.vue'
import Navbar from './components/Navbar.vue'
import NewItem from './components/NewItem.vue'

  export default{
    name: 'App',
    data(){
      return{
        users: [],
        user:{
          'username': '',
          'userEmail': '',
          'userDateOfBirth': '',
          'userImage': '',
        },
        auctions: [],
        auction : {
          'itemTitle':'',
          'itemDescription':'',
          'itemStartPrice':'',
          'itemPicture': '',
          'itemFinishDate':'',
          'ownerId':'',
        },
        bids : [],
        bid : {
          'userId': '',
          'bidAmount': '',
          'auctionId':'',
        }
      } 
    },

    async created(){
       await this.getUsers();
       console.log(this.users);
      },
    methods:{

      submitUser(){
        if(this.user.id ===undefined){
          this.addUser();
        }
        else{
          this.updateUser();
        }
      },

      async getUsers(){
        var response = await fetch("http://127.0.0.1:8000/api/users/")
        let data = await response.json()
        this.users = data 
      },

      async addUser(){
        await this.getUsers();
        await fetch("http://127.0.0.1:8000/api/users/",{
          method: 'post',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.user)  
        });
        await this.getUsers();
        this.user = {};
      },

      

      async updateUser(){
        await this.getUsers();
        await fetch(`http://127.0.0.1:8000/api/users/${this.user.id}/`,{
          method: 'put',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.user)  
        });
        await this.getUsers();
        this.user = {};
      },

      async deleteUser(user){
        await this.getUsers();
        await fetch(`http://127.0.0.1:8000/api/users/${user.id}/`,{
          method: 'delete',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.user)  
        });
        await this.getUsers();
      },

      submitAuction(){
        if(this.auction.id ===undefined){
          this.addAuction();
        }
        else{
          this.updateAuction();
        }
      },

      async getAuctions(){
        var response = await fetch("http://127.0.0.1:8000/api/auctions/")
        let data = await response.json()
        this.auctions = data 
      },

      async addAuction(){
        await this.getAuction();
        await fetch("http://127.0.0.1:8000/api/auctions/",{
          method: 'post',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.auction)  
        });
        await this.getAuctions();
        this.auction = {};
      },

      async updateAuction(){
        await this.getAuctions();
        await fetch(`http://127.0.0.1:8000/api/auctions/${this.auction.id}/`,{
          method: 'put',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.auction)  
        });
        await this.getAuctions();
        this.auction = {};
      },

      async deleteAuction(auction){
        await this.getAuctions();
        await fetch(`http://127.0.0.1:8000/api/users/${auction.id}/`,{
          method: 'delete',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.auction)  
        });
        await this.getAuctions();
      },

      submitBid(){
        if(this.bid.id ===undefined){
          this.addBid();
        }
        else{
          this.updateBid();
        }
      },

      async getBids(){
        var response = await fetch("http://127.0.0.1:8000/api/bids/")
        let data = await response.json()
        this.bids = data 
      },

      async addBid(){
        await this.getBids();
        await fetch("http://127.0.0.1:8000/api/bids/",{
          method: 'post',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.bid)  
        });
        await this.getBids();
        this.bid = {};
      },

      async updateBid(){
        await this.getBids();
        await fetch(`http://127.0.0.1:8000/api/bids/${this.bid.id}/`,{
          method: 'put',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.bid)  
        });
        await this.getBids();
        this.bid = {};
      },

      async deleteBid(bid){
        await this.getBids();
        await fetch(`http://127.0.0.1:8000/api/bids/${bid.id}/`,{
          method: 'delete',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.bid)  
        });
        await this.getBids();
      }
    },

    
      name: 'app',
      components: {
      Navbar,
      Home,
      NewItem,
      Profile,
  }

  }
</script>



<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
