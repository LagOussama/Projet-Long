import { Component, OnInit } from '@angular/core';
import {NetworkService} from "../service/network.service";
import {Network} from "../common/network";

@Component({
  selector: 'app-index',
  templateUrl: './index.component.html',
  styleUrls: ['./index.component.css']
})
export class IndexComponent implements OnInit {

  networks: Array<Network> = []



  constructor(private networkService:NetworkService) { }


  ngOnInit(): void {
    this.getNetworkList();
  }

   getNetworkList() {
     let netw = new Network();
     netw.adress= "192.168.1.1"
     netw.description = "Network 1"
     netw.hosts = "15"
     netw.addedOn = new Date();

       console.log(netw)

     this.networks.push(netw)


     // this.networkService.getNetwork().subscribe(
     //   data => {
     //     this.networks = data;
     //   }, error => {
     //     console.log(error);
     //
     //   });
   }
}
