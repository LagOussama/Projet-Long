import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {HttpClientModule} from "@angular/common/http";
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { IndexComponent } from './index/index.component';
import {RouterModule, Routes} from "@angular/router";
import { HostComponent } from './host/host.component';
import {NetworkService} from "./service/network.service";
import {HostService} from "./service/host.service";
import { HostDetailsComponent } from './host-details/host-details.component';
<<<<<<< HEAD
import { InterfaceComponent } from './interface/interface.component';
=======
import { HostPlotComponent } from './host-plot/host-plot.component';
>>>>>>> 8644c72b1c60b6620ea0c6eae60d5d18cb1c593a

const routes:Routes = [
  {path:'index',component:IndexComponent},
  {path:'host',component:HostComponent},
  {path:'plot',component:HostPlotComponent},
  {path: 'host/:hostId', component: HostDetailsComponent},
  {path: 'host/:hostId/:hostId', component: HostDetailsComponent},

  {path:'', redirectTo:'/index',pathMatch:'full'}


];
@NgModule({
  declarations: [
    AppComponent,
    IndexComponent,
    HostComponent,
    HostDetailsComponent,
    InterfaceComponent,
    HostPlotComponent
  ],
  imports: [
    HttpClientModule,
    BrowserModule,
    AppRoutingModule,
    RouterModule.forRoot(routes)
  ],
  providers: [NetworkService,HostService],
  bootstrap: [AppComponent]
})
export class AppModule { }
