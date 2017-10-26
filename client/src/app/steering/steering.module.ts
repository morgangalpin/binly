import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { MatCardModule, MatSliderModule } from '@angular/material';

import { SteeringComponent } from './steering.component';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    MatCardModule,
    MatSliderModule
  ],
  declarations: [SteeringComponent],
  exports: [SteeringComponent],
  providers: []
})
export class SteeringModule { }
