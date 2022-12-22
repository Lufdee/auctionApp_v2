<template >

<div class="home">
    <br/>
<h1> Listings </h1>
<div class="d-grid gap-2 col-6 mx-auto">
    <button class="btn btn-primary" type="submit"> <router-link to="/newitem" class="nav-link">New Item</router-link></button>
</div>
<br/>
<div class="row">
  <div class="input-group" style="margin-bottom:1rem;">
    <input type="search" class="form-control rounded" placeholder="Search" />
    <button type="button" class="btn btn-outline-primary">Search</button>
  </div>
  
<table class="table border rounded bg-light shadow">
        <thead>
          <tr>
            <th scope="col">Item Title</th>
            <th scope="col">Image</th>
            <th scope="col">Start Price</th>
            <th scope="col">Ending</th>
          </tr>
        </thead>
        <tbody class="align-middle" v-for="auction in auctions" :key="auction.itemFinishDate" @dblclick="$data.auction = auction">
          <tr style="background:#E1E1E1;" >
              <td v-if="skippableDate(auction.itemFinishDate)">{{auction.itemTitle}} </td>
              <td v-if="skippableDate(auction.itemFinishDate)"> <img :src="auction.itemPicture.substring(39)" width="100"/></td>
              <td v-if="skippableDate(auction.itemFinishDate)">{{auction.itemStartPrice}} </td>
              <td v-if="skippableDate(auction.itemFinishDate)">{{auction.itemFinishDate}}</td>
              <td v-if="skippableDate(auction.itemFinishDate)"></td>
              <td v-if="skippableDate(auction.itemFinishDate)">
                <tr ><input type=number min="0"/></tr>
                <tr><button type="button" class="btn btn-primary">Bid Amount</button></tr>
              </td>
              <td v-if="skippableDate(auction.itemFinishDate)">
                <tr><textarea/></tr>
                <tr><button type="button" class="btn btn-primary">Submit Question</button></tr>
              </td>
    
            </tr>
          
          
          <tr v-if="skippableDate(auction.itemFinishDate)"> 
            <th></th> <!-- Leave Empty -->
            <th scope="col">Questions</th>
          </tr>
          <tr v-if="skippableDate(auction.itemFinishDate)">
            <th></th> <!-- Leave Empty -->
            <th scope="col">User</th>
            <th scope="col">Question</th>
          </tr>
          
          <tr v-for="question in questions" :key="question.questionId">  
            <td></td> <!-- Leave Empty -->
            <td>{{question.userId}}</td> <!-- GET Userid from question -->
            <td>{{question.questionText}}</td> <!-- GET question from question -->

            <tr>
              <th></th> <!-- Leave Empty -->
              <th></th> <!-- Leave Empty -->
              <th scope="col">Answer</th>
              
            </tr>

            <tr>
              <td></td> <!-- Leave Empty -->
              <td></td> <!-- Leave Empty -->
              <td></td> <!-- Leave Empty -->
              <td>
                <tr><textarea/></tr>
                <tr><button type="button" class="btn btn-primary">Submit Answer</button></tr>
              </td>
            </tr>

          </tr>

          
          


        </tbody>
      </table>

</div>

</div>
</template>

<script>

 
        
  export default{
    name: 'Home',
    data(){
      return{
        questions: [],
        question:{
          'auctionId':'',
          'questionText':'',
          'userId':'',
        },
        answers:[],
        answer:{
          'questionId': '',
          'answerText': '',
          'userId': '',
        },
        auctions: [],
        auction:{
          'itemTitle':'',
          'itemDescription':'',
          'itemStartPrice':'',
          'itemPicture': '',
          'itemFinishDate':'',
          'ownerId':'',  
        }
      }
    },
    async created(){
       await this.getAuctions();
      },
      methods:{

      async getAuctions(){
        var response = await fetch("http://127.0.0.1:8000/api/auction/")
        let data = await response.json()
        this.auctions = data 
      },

      async addAuction(){
        await this.getAuctions();
        await fetch("http://127.0.0.1:8000/api/auction/",{
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
        await fetch(`http://127.0.0.1:8000/api/auction/${this.auction.id}/`,{
          method: 'put',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.auction)  
        });
        await this.getAuctions();
        this.auction = {};
      },

      skippableDate(date){
            var now = new Date();
            var skippableDate = now.setDate(now.getDate())  // this is getting next thursday
	    var parseDate = Date.parse(date);

            if(parseDate > skippableDate){
                return true
            }else{
                return false
            }
        }

      }

  }

  
 
</script>