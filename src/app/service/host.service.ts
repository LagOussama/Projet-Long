import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class HostService {

  public host:string="http://localhost:8080"

  constructor(private httpClient : HttpClient) { }

  getHost(){
    return this.httpClient.get(this.host+"/networks");
  }

  public getHostByKeyword(mc:string){
    console.log(mc);
    return this.httpClient.get(this.host+"/hosts/search/byAdrMac?mc="+mc);
  }
}
