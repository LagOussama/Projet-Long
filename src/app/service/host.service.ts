import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Host} from "../common/host";

@Injectable({
  providedIn: 'root'
})
export class HostService {

  public host:string="http://localhost:5000"

  constructor(private httpClient : HttpClient) { }

  getHost(){
    return this.httpClient.get(this.host+"/host");
  }

  public getHostByKeyword(mc:string){
    console.log(mc);
    return this.httpClient.get(this.host+"/host/?mc="+mc);
  }

  public getResource(url){


    return this.httpClient.get(this.host+"/host/"+url);
  }
}
