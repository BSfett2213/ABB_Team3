import { ComponentFixture, TestBed } from '@angular/core/testing';

import { StepProgress } from './step-progress';

describe('StepProgress', () => {
  let component: StepProgress;
  let fixture: ComponentFixture<StepProgress>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [StepProgress]
    })
    .compileComponents();

    fixture = TestBed.createComponent(StepProgress);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
