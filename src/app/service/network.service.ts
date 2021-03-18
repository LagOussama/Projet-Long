import { Injectable } from '@angular/core';

import {HttpClient} from "@angular/common/http";
import {map} from "rxjs/operators";

@Injectable({
  providedIn: 'root'
})
export class NetworkService {

  public host:string="http://localhost:5000"

  constructor(private httpClient : HttpClient) { }

  getNetwork(){
    console.log( this.httpClient.get(this.host+"/network"));
    return this.httpClient.get(this.host+"/network");
  }

  getByProtocol(){
    return this.httpClient.get(this.host+"/protocol");
  }

  getNbPacket(){
    return this.httpClient.get(this.host+"/protocol/nbPacket");
  }

  getNbHost(){
    return this.httpClient.get(this.host+"/host");
  }
}

