import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';

@NgModule({
  imports: [BrowserModule, AppComponent], // import standalone component here
  bootstrap: [AppComponent],             // bootstrap it
})
export class AppModule {}
