import { Component, OnInit } from '@angular/core';
import {NetworkService} from "../service/network.service";
import {Network} from "../common/network";
import  {hosts} from "../hosts"

@Component({
  selector: 'app-index',
  templateUrl: './index.component.html',
  styleUrls: ['./index.component.css']
})
export class IndexComponent implements OnInit {

  public networks: any;
  hostNumb : number

  constructor(private networkService:NetworkService) { }


  ngOnInit(): void {
    this.getNetworkList();

    this.hostNumb = hosts.length;


  }

   getNetworkList() {
      this.networkService.getNetwork().subscribe(
        data => {
          this.networks = data;
        }, error => {
          console.log(error);

        });
   }
}
