import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { PpListComponent } from './pp-list.component';
import { PpDetailComponent } from './pp-detail.component';

@NgModule({
  declarations: [
    AppComponent,
    PpListComponent,
    PpDetailComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
